import os
import jpype
import tabula
from tqdm import tqdm

failures = 0


def convert(pdf):
    # takes PDF, returns CSV in same directory as pdf

    # replace '.pdf' with '.csv'
    csv = pdf.replace(".pdf", ".csv")

    # use tabula to make a dataframe from the PDF and save it as a CSV
    try:
        df = tabula.read_pdf(pdf, pages="all")[0]
        df.to_csv(csv)
    except IndexError:
        global failures
        failures += 1
        print(f'Failed on {pdf}')


if __name__ == "__main__":
    # setting path to transcript files, change as appropriate for your files
    # note: the final '/' is important here
    path = "/home/wassu/Documents/Transcripts/"

    # get names of PDF files at this path
    files = os.listdir(path)
    pdfs = [path + file for file in files if file[-4:] == ".pdf"]

    # send each PDF for conversion to CSV
    for pdf in tqdm(pdfs):
        convert(pdf)

    successes = len(pdfs) - failures
    print(f"Done! Converted {successes} files")
