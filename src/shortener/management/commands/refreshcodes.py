from django.core.management.base import BaseCommand, CommandError

from shortener.models import VtuURL


class Command(BaseCommand):
	help = 'Refresh all VtuURL shortcodes'

	def add_arguments(self, parser):
		parser.add_argument('--items', type=int)

	def handle(self, *args, **options):
		print(options)
		return VtuURL.objects.refresh_shortcodes(items=options['items'])