from django.http import JsonResponse

from sudoku.puzzle import make_new_puzzle, remove_numbers_from_puzzle

from django.shortcuts import render


def puzzle(request):
    n_attempts, puzzle =  make_new_puzzle()

    output = {
        'n_attempts': n_attempts,
        'puzzle' : puzzle
    }

    return JsonResponse(output)


def home(request):
    n_attempts, sudoku_puzzle = make_new_puzzle()
    level = 'easy'
    sudoku_puzzle_with_holes = remove_numbers_from_puzzle(sudoku_puzzle, level)

    context = {
        'sudoku_puzzle': sudoku_puzzle,
        'n_attempts': n_attempts, 
        'sudoku_puzzle_with_holes': sudoku_puzzle_with_holes,
        'level': level,
    }
    
    return render(request, 'home.html', context)