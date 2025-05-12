from django.db import models
from django.urls import reverse
from django.conf import settings
from openai import OpenAI

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    summary = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )

        completion = client.chat.completions.create(
            model="bytedance-research/ui-tars-72b:free",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this text in 30 words: '{self.body}'"
                }
            ]
        )

        self.summary = completion.choices[0].message.content

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post}'
    
    class Meta:
        ordering = ['created']