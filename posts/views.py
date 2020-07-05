from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

#Now we created the functions

#esta para ver todas la publicaciones anteriores, link con un html concreto
def get_posts(request):
    """
    create a view that will return a list of posts that were published before.
    And render them to a template called blogposts.html
    """
    post = Post.objects.filter(published_date__lt=timezone.now()).order_by('-published_date')
    return render(request, 'blogposts.html', {'posts' : posts}) # this last part send back our posts object ( where?)



#esta para examinar en mas detalle cada uno de los post segun su ID(pk), check metadata
def post_detail(request, pk):
    """
    Create a view that returns a single post object based on the post ID, which is pk,
    and then render it to the postdetail.html template or return an error if the post
    is not found.
    """
    post = get_object_or_404(Post, pk =pk)
    post.views += 1
    post.save()
    return render(request, 'postdetail.html', {'posts':posts})



#este para editar un post si ya tiene ID (esta creado) o para crearlo si no lo tiene
def create_or_edit_post(request, pk=None):
    """
    create a view that allows us to create or edit a post, depending if the post ID
    is null or not.
    """
    #create an object here again
    post = get_object_or_404(Post,pk=pk ) if pk else None
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'blogpostform.html', {'form': form}) #send back the form


