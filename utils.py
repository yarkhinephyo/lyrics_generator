import os
import json

def get_genres():
    data_files = os.listdir('static')
    genres = []

    for data_file in data_files:
        genres.append(data_file.split("_")[0])
    return genres

def validate_input(request):

    errs = []
    genre = request.args.get('genre')
    rhyme_freq = request.args.get('rhyme_freq', type=int)
    max_length = request.args.get('max_length', type=int)
    num_lines = request.args.get('max_length', type=int)

    if not genre:
        errs.append('Please select genre')
    if max_length < 2:
        errs.append('Please select longer max_length')
    if num_lines < 4 or num_lines < rhyme_freq:
        errs.append('Number of lines too short')
    
    return json.dumps(errs), genre, rhyme_freq, max_length, num_lines

# print(get_genres())