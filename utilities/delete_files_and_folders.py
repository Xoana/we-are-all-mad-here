import os
import sys
import logging
import shutil
import click
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

logging.basicConfig(level=logging.INFO, format='%(message)s')

@click.command()
@click.option("--target_folder", default="", show_default=True,
              help="Path to the folder from which to delete files.")
@click.option("--target_date", type=click.DateTime(formats=["%Y-%m-%d"]), show_default=True,
              default=str(date.today()-relativedelta(months=3)), help="Target date in the following format: YYYY-MM-DD; files dated on or before this date will be deleted. The default date is today's date minus 3 months.")
@click.option("--skip_delete", is_flag=True,
              help="Flag used to skip deleting files; can be used to review the list of files before deleting.")
def main(target_folder,target_date,skip_delete):
    ''' Delete files and subfolders from the specified target folder with a modified date on or before the specified date. 
        
        Tip: Use the --skip_delete option and &> to output the list of files and folders to a text file for review.
        
        For example:
        
        python delete_files.py --target_date 2022-11-01 --target_folder ./path_to_folder/ --skip_delete &> output.log
    '''

    target_date_str = target_date.strftime("%Y-%m-%d")
    logging.info('>>>>> Deleting files with modified date on or before %s. <<<<<', target_date_str)
    target_date_epoch = datetime.strptime(target_date_str, "%Y-%m-%d").timestamp()
    for path, sub_directories, file_list in os.walk(target_folder):

        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            if (os.stat(file_path).st_mtime <= target_date_epoch+86400):
                logging.info('Deleting file: %s',file_path)
                if not skip_delete:
                    try:
                        os.remove(file_path)
                    except Exception as remove_exc:
                        logging.info('Removing the file failed with the following exception: %s',remove_exc)
                        sys.exit(1)

        for sub_directory in sub_directories:
            sub_directory_path = os.path.join(path, sub_directory)
            if (os.stat(sub_directory_path).st_mtime <= target_date_epoch+86400):
                logging.info('Deleting directory: %s',sub_directory_path)
                if not skip_delete:
                    try:
                        shutil.rmtree(sub_directory_path)
                    except Exception as rmdir_exc:
                        logging.info('Removing the directory failed with the following exception: %s',rmdir_exc)
                        sys.exit(1)


if __name__ == "__main__":
    main()