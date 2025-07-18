from pytrends.request import TrendReq

def get_trending_keywords(limit=10, geo='KR'):
    try:
        pytrends = TrendReq(hl='ko', tz=540)
        pytrends.build_payload(kw_list=[""])
        trending_searches_df = pytrends.trending_searches(pn='south_korea')
        trending_keywords = trending_searches_df[0].tolist()[:limit]
        return trending_keywords
    except Exception as e:
        print(f"[❌ Google Trends Error]: {e}")
        return ["트렌드 없음"]
