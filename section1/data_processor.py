import pandas as pd 
from datetime import datetime

class AssignmentDataProcessor:
    def __init__(self) -> None:
        pass

    def preprocessor(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = [col.lower().strip().replace(' ', '_') for col in  df.columns] 
        df['birth_year'] = df['birth_year'].astype('Int64')
        df.dropna(inplace=True)
        return df 

    @classmethod
    def age_mapper_producer(self, df: pd.DataFrame) -> dict[str, int]:
        df.sort_values('birth_year', inplace=True)
        age_mapper = {}
        for index, row in df.iterrows():
            age_mapper[row['name']] = row['birth_year']
        return age_mapper

    @classmethod
    def group_by_age(self, age_mapper: dict[str, int]):
        gba_mapper, index, temp = {}, 0, 0
        for name, year in age_mapper.items():
            if year == temp: 
                gba_mapper[index].append(name) 
            else: 
                index+=1
                gba_mapper[index] = [name]               
            temp = year
        return gba_mapper

    @classmethod
    def middle_vowel_names(self, names: list[str]) -> list[str]:
        vowel = ['a', 'e', 'i', 'o', 'u']
        return [name for name in names if (len(name)%2!=0 and name[int(len(name)/2)] in vowel )]

    @classmethod
    def age_group_converter(self, value: int):
        age = datetime.now().year - value
        if age < 18: 
            return 'TEENAGER'
        elif 18 <= age <= 40:
            return 'YOUNG'
        elif age >= 40: 
            return 'OLD'
    
    @classmethod
    def age_calculator(self, value: int):
        return datetime.now().year - value

    @classmethod
    def avg_age_calculator(self, df: pd.DataFrame, value: str):
        return int(df[df['age_group']==value]['age'].mean())

    @classmethod
    def grade_calculator(self, a:int, b:int, mid:int, project:int, final:int):
        a = (a/100*7) if a != 0 else 0
        b = (b/100*13) if b != 0 else 0  
        mid = (mid/100*20) if mid != 0 else 0   
        project = (project/100*25) if project != 0 else 0   
        final = (final/100*35) if final != 0 else 0 
        return a + b + mid + project + final 




