import pandas as pd
from config import get_path


df = pd.DataFrame(pd.read_csv(get_path()+'amount.csv'))

print df




