import os

from pypdf import PdfWriter


def compress_n_update(pdf_file_dir,pdf_filename):
    pdf_filepath = os.path.join(pdf_file_dir, pdf_filename)
    writer = PdfWriter(clone_from=pdf_filepath)

    for page in writer.pages:
        page.compress_content_streams()  # This is CPU intensive!


    # Split filename and extension
    filename, extension = os.path.splitext(pdf_filename)

    # Create new filename
    new_filename = f"{filename}_compress{extension}"
    new_filepath = os.path.join(pdf_file_dir, new_filename)

    print(f"compress_n_update filename: {pdf_filename}")
    with open(new_filepath, "wb") as f:
        writer.write(f)

    old_filesize = os.path.getsize(pdf_filepath)
    new_filesize = os.path.getsize(new_filepath)
    print(f"the file size of filename: {pdf_filename} is {old_filesize}")
    print(f"the file size of filename: {new_filename} is {new_filesize}")
    if old_filesize <= new_filesize:
        os.remove(new_filepath)
        print(f"remove the file {pdf_filename} successfully")
        return
    os.remove(pdf_filepath)
    os.rename(new_filename,pdf_filename)
    print(f"Renamed {pdf_filename} to {new_filename}")
if __name__ == "__main__":
    current_dir = "./2AT7UNZU"
    compress_n_update("./2AT7UNZU",[f for f in os.listdir(current_dir) if f.lower().endswith('.pdf')][0])