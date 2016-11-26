from django.conf import settings
from django.http import HttpResponseRedirect

DFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.vtuurls.com")

def wildcard_redirect(request, path=None):
	new_url = DEFAULT_REDIRECT_URL
	if path is not None
		new_url = DEFAULT_REDIRECT_URL + "/" + path
	return HttpResponseRedirect(new_url)