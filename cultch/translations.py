from urllib.parse import unquote

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import translate_url
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils import translation


LANGUAGE_QUERY_PARAMETER = 'language'


def set_language(request):
    """
    Redirect to a given URL while setting the chosen language in the session
    (if enabled) and in a cookie. The URL and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next_url = request.GET.get('next')
    allowed = url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    )
    nxt_url = next_url or request.accepts('text/html')
    if nxt_url and not allowed:
        next_url = request.META.get('HTTP_REFERER')
        # HTTP_REFERER may be encoded.
        next_url = next_url and unquote(next_url)
        if not url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
        ):
            next_url = '/'
    response = HttpResponseRedirect(
        next_url
    ) if next_url else HttpResponse(status=204)
    lang_code = request.GET.get(LANGUAGE_QUERY_PARAMETER)
    if lang_code and translation.check_for_language(lang_code):
        if next_url:
            next_trans = translate_url(next_url, lang_code)
            if next_trans != next_url:
                response = HttpResponseRedirect(next_trans)
        if hasattr(request, 'session'):
            # Storing the language in the session is deprecated.
            # (RemovedInDjango40Warning)
            # request.session[settings.LANGUAGE_SESSION_KEY] = lang_code
            pass
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, lang_code,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=settings.LANGUAGE_COOKIE_SECURE,
            httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
            samesite=settings.LANGUAGE_COOKIE_SAMESITE,
        )
    return response
