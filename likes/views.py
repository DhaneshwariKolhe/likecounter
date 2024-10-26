from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from likes.models import Post
from likes.kafka_producer import *


def post_like(request, post_id):
    send_like_event(post_id)
    # post = Post.objects.get(id = post_id)
    # post.like += 1
    # post.save()
    return JsonResponse({
        "status": True,
        "message": "like incremented"
    })