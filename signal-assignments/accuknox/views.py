from django.http import HttpResponse
from django.db import transaction
from .models import YashasBlogPost, YashasComment
import time
import threading

def create_yashas_blogpost(request):
    start_time = time.time()
    current_thread = threading.current_thread()
    print(f"View starting at {start_time} in thread: {current_thread.name} (ID: {current_thread.ident})")

    try:
        with transaction.atomic():
            post = YashasBlogPost.objects.create(
                title="Yashas' Django Signals Adventure",
                content="Join Yashas as he explores the intricacies of Django signals!",
                author="Yashas"
            )
            print(f"Created YashasBlogPost with id {post.id}")

            
    except Exception as e:
        print(f"Exception occurred: {str(e)}")

    end_time = time.time()
    print(f"View finished at {end_time}")
    print(f"Total view execution time: {end_time - start_time} seconds")

    # Check final state
    post_count = YashasBlogPost.objects.count()
    comment_count = YashasComment.objects.count()
    print(f"Final YashasBlogPost count: {post_count}")
    print(f"Final YashasComment count: {comment_count}")

    return HttpResponse("Yashas' BlogPost creation attempted")
