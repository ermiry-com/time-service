import signal

import cerver

from cache import ermiry_cache_init
from ermiry import ermiry_config, ermiry_init
import service
import version

if __name__ == "__main__":
	signal.signal (signal.SIGINT, service.end)
	signal.signal (signal.SIGTERM, service.end)
	signal.signal (signal.SIGPIPE, signal.SIG_IGN)

	cerver.cerver_init ()

	cerver.cerver_version_print_full ()

	cerver.pycerver_version_print_full ()

	version.ermiry_time_version_print_full ()

	ermiry_config ()

	if (ermiry_cache_init ()):
		ermiry_init ()
		
		service.start ()
