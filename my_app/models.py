from django.db import models


class Search(models.Model):
    # models.XXXFields will return a class instance
    search = models.CharField(max_length=500)
    created = models.DateField(auto_now=True)

    def __str__(self):
        """
        display the text of the search
        instead of the object-info: "Search object(1)"
        :return:
        """
        # return f"{self.search}"
        return f"{self.id}. {self.search}"

    class Meta:
        verbose_name_plural = 'Searches'  # modify searchs to searches
