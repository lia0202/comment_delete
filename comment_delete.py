# тесты не падают
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

# тесты падают с ошибкой nonetype
@login_required
def comment_delete(request, pk, comment_id):
    comment = get_object_or_404(Comment.objects.select_related('post'),
                                id=comment_id, post__pk=pk)
    if comment.author.username != request.user.username:
        return redirect('blog:post_detail', pk=pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('blog:post_detail', pk=pk)

# работающий код post_delete
@login_required(login_url='blog:index')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author.username != request.user.username:
        return redirect('blog:index')

    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return redirect('blog:index')
