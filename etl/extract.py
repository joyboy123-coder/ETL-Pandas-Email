import pandas as pd  

def extract_data():
    print('================================================================')
    input_file = input('📂 Enter your file path from the raw folder: ').strip('"')
    df = pd.read_csv(input_file)
    
    print()
    print('✅ Extracted Data Successfully!')
    print('🧼 On to clean some messy data...')
    print('===========================================')


