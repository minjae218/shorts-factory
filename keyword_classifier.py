def classify_keyword_to_category(keyword):
    keyword = keyword.lower()

    if "키즈" in keyword or "아이" in keyword or "어린이" in keyword:
        return "kids"
    elif "캠핑" in keyword or "텐트" in keyword:
        return "camping"
    elif "출시" in keyword or "신제품" in keyword or "신상" in keyword:
        return "new_products"
    elif "팁" in keyword or "생활" in keyword or "꿀팁" in keyword:
        return "useful_tips"
    elif "여행" in keyword or "관광" in keyword:
        return "korea_travel"
    elif "연예인" in keyword or "배우" in keyword or "아이돌" in keyword:
        return "kcelebs"
    elif "한국" in keyword or "이민" in keyword or "사는법" in keyword:
        return "life_in_korea"
    else:
        return "useful_tips"  # 기본값
