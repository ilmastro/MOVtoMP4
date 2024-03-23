import subprocess

def convert_mov_to_mp4(mov_file_path, output_mp4_file_path):
    """
    Convert a .mov file to .mp4 format using FFmpeg.

    Args:
    - mov_file_path: The path to the .mov file.
    - output_mp4_file_path: The path where the .mp4 file will be saved.
    """
    command = ['ffmpeg', '-i', mov_file_path, '-q:v', '0', output_mp4_file_path]
    subprocess.run(command)

# Example usage:
mov_file_path = 'mov_files'
output_mp4_file_path = 'out_put_mp4'
convert_mov_to_mp4(mov_file_path, output_mp4_file_path)
