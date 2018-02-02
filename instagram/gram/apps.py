from django.apps import AppConfig


class GramConfig(AppConfig):
    name = 'gram'


# class GramAppConfig(GramConfig):
#     def ready(self):
#     story_model = apps.get_model("story_", "Story")
#     secretballot.enable_voting_on(story_model)