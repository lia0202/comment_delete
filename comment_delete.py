@login_required
def comment_delete(request, pk, comment_id):
    form = CommentForm
    comment = get_object_or_404(Comment.objects.select_related('post'),
                                id=comment_id, post__pk=pk)
    if comment.author.username != request.user.username:
        return redirect('blog:post_detail', pk=pk)
    if request.method == 'POST':
        comment.delete()
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'form': form,
        'pk': pk,
    }
    return render(request, 'blog/detail.html', context)
