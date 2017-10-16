from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from map.models import MajorReservoirs, StoryContent


@receiver(post_save, sender=StoryContent)
def enable_lake(sender, **kwargs):
    instance = kwargs['instance']
    # update major reservoir to enabled in app
    r = MajorReservoirs.objects.get(res_lbl=str(instance.lake))
    r.story = 'enabled'
    r.save()


@receiver(post_delete, sender=StoryContent)
def disable_lake(sender, **kwargs):
    instance = kwargs['instance']
    # update major reservoir to disabled in app
    r = MajorReservoirs.objects.get(res_lbl=str(instance.lake))
    r.story = 'disabled'
    r.save()
