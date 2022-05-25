from cerver.utils import LOG_TYPE_NONE, cerver_log_both

ERMIRY_VERSION = "0.1"
ERMIRY_VERSION_NAME = "Version 0.1"
ERMIRY_VERSION_DATE = "24/05/2022"
ERMIRY_VERSION_TIME = "23:02 CST"
ERMIRY_VERSION_AUTHOR = "Erick Salas"

service_version = {
	"name": ERMIRY_VERSION_NAME,
	"date": ERMIRY_VERSION_DATE,
	"time": ERMIRY_VERSION_TIME,
	"author": ERMIRY_VERSION_AUTHOR
}

def ermiry_time_version_print_full ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nErmiry Time Version: %s".encode ("utf-8"),
		ERMIRY_VERSION_NAME.encode ("utf-8")
	)

	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"Release Date & time: %s - %s".encode ("utf-8"),
		ERMIRY_VERSION_DATE.encode ("utf-8"),
		ERMIRY_VERSION_TIME.encode ("utf-8")
	)

	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"Author: %s\n".encode ("utf-8"),
		ERMIRY_VERSION_AUTHOR.encode ("utf-8")
	)

def ermiry_time_version_print_version_id ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nErmiry Time Version ID: %s\n".encode ("utf-8"),
		ERMIRY_VERSION.encode ("utf-8")
	)

def ermiry_time_version_print_version_name ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nErmiry Time Version: %s\n".encode ("utf-8"),
		ERMIRY_VERSION_NAME.encode ("utf-8")
	)
