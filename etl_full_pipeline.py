from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load

def main():

    extract_data()
    transform_data()
    load()



if __name__ == "__main__":
    main()