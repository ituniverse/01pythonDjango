from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.contrib.auth.decorators import login_required


# 목록 출력
def board_list(request):
    # list = Board.objects.filter(modify_date__lte=timezone.now()).order_by('modify_date')
    list = Board.objects.order_by('-modify_date')
    return render(request, 'board/board_list.html', {'list': list})


# 목록 상세
def board_detail(request, pk):
    boardOne = get_object_or_404(Board, pk=pk)
    return render(request, 'board/board_detail.html', {'boardOne': boardOne})


# 목록 등록
@login_required
def board_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.writer = request.user
            board.modify_date = timezone.now()
            board.save()
            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardForm()
        return render(request, 'board/board_edit.html', {'form': form})


# 게시글 수정
@login_required
def board_edit(request, pk):
    print("수정 진입")
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.writer = request.user
            board.modify_date = timezone.now()
            board.save()
            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)
    return render(request, 'board/board_edit.html', {'form': form})


# draft
@login_required
def board_draft_list(request):
    list = Board.objects.filter(modify_date__isnull=True).order_by('created_date')
    return render(request, 'board/board_draft_list.html', {'list': list})


# 출판
@login_required
def board_publish(request, pk):
    print("출판 진입")
    board = get_object_or_404(Board, pk=pk)
    board.publish()
    return redirect('board_detail', pk=pk)


# 삭제
@login_required
def board_remove(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('board_list')


# 코멘트 달기
def add_board_comment(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
            return redirect('board_detail', pk=board.pk)
    else:
        form = CommentForm()
    return render(request, 'board/add_board_comment.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('board_detail', pk=comment.board.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    board_pk = comment.board.pk
    comment.delete()
    return redirect('board_detail', pk=board_pk)