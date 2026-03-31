import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]    
    unique_ids = df['author_id'].unique()    
    res = pd.DataFrame({'id': unique_ids})
    res = res.sort_values(by='id')    
    return res
