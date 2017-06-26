from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
                {
                    "type": "doctype",
                    "name": "PAYE Tax Years"
                },
                {
                    "type": "doctype",
                    "name": "PAYE Employee Tax"
                },
			]
		},
	]