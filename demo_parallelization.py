from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import Pool
from pathlib import Path

from knotprot_download import get_proteins, download_link, setup_download_dir, time_it, create_thumbnail


def run_download_seq(my_dir):
    prot_list = get_proteins()
    i = 0
    for prot in prot_list:
        i += 1
        download_link(my_dir, prot)
    print(f'Downloaded {i} proteins.')


def run_download_parall(my_dir):
    prot_list = get_proteins()
    download_func = partial(download_link, my_dir)
    with Pool(processes=16) as pool:
        pool.map(download_func, prot_list)


def run_thumbnails_seq(my_dir):
    file_list = Path(my_dir).iterdir()
    for f in file_list:
        create_thumbnail((324, 324), f)


def run_thumbnails_parall(my_dir):
    file_list = Path(my_dir).iterdir()
    create_thumbnail_func = partial(create_thumbnail, (324, 324))
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(create_thumbnail_func, file_list)
    # with Pool(processes=16) as pool:
    #     pool.map(create_thumbnail_func, file_list)

if __name__ == '__main__':
    my_dir = 'images'
    #setup_download_dir(my_dir)
    #run_download_seq(my_dir)
    #time_it(run_download_seq, my_dir)
    #time_it(run_download_parall, my_dir)
    #time_it(run_thumbnails_seq, my_dir)
    time_it(run_thumbnails_parall, my_dir)