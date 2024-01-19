import sys
from audiomixer.segmentation.segment import segment

if __name__ == "__main__":
    """
    ignore 1st argument because it will be 'main.py'
    sample command:

    $python main.py src_path dest_path
    """
    args = sys.argv[1:]
    segment(*args)
