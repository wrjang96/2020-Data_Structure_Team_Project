# 음식점 명단 리스트
Flist = [
    "후쿠후쿠",
    "노가네",
    "홍순두부",
    "삼삼오오",
    "째즈앤라멘",
    "돈앤까",
    "쇼타돈부리",
    "청춘직화",
    "저팔계",
    "천하탕수육",
    "홍곱창",
    "샐러드온",
    "BBQ",
    "산조메",
    "명륜쭈꾸미",
    "casa 14-2",
    "밴프",
    "천향록",
    "페르시안궁전",
    "맥덕스",
    "포보",
    "맥도날드",
    "나누미떡볶이",
    "따띠삼겹",
    "이삭토스트",
    "성균원",
    "할매순대국",
    "다발 김치찌개",
    "60계치킨",
    "명륜왕만두",
]

# 위치별 분류 리스트
# 쪽문
Sdoor = ["후쿠후쿠", "노가네", "홍순두부", "삼삼오오", "째즈앤라멘", "돈앤까", "쇼타돈부리", "청춘직화", "저팔계", "천하탕수육"]

# 철문(정문 쪽문 사이 포함)
Idoor = ["홍곱창", "샐러드온", "BBQ", "산조메", "명륜쭈꾸미", "casa 14-2", "밴프"]

# 정문
Fdoor = [
    "천향록",
    "페르시안궁전",
    "맥덕스",
    "포보",
    "맥도날드",
    "나누미떡볶이",
    "따띠삼겹",
    "이삭토스트",
    "성균원",
    "할매순대국",
    "다발 김치찌개",
    "60계치킨",
    "명륜왕만두",
]

# 메뉴별 분류 리스트
# 양식
west = ["샐러드온", "casa 14-2", "맥덕스", "밴프", "이삭토스트"]
# 한식
korea = [
    "삼삼오오",
    "청춘직화",
    "홍순두부",
    "명륜쭈꾸미",
    "노가네",
    "나누미떡볶이",
    "따띠삼겹",
    "다발 김치찌개",
    "할매순대국",
    "홍곱창",
    "명륜왕만두",
]
# 중식
china = ["천하탕수육", "저팔계", "천향록", "성균원"]
# 일식
japan = [
    "후쿠후쿠",
    "째즈앤라멘",
    "돈앤까",
    "쇼타돈부리",
    "산조메",
]
# fastfood
fastfood = ["맥도날드", "60계치킨", "BBQ"]
# 기타
etc = ["포보", "페르시안궁전"]
# 음식점 이름 딕셔너리
후쿠후쿠 = {"가츠동": 6000, "믹스동": 7000, "규동": 6500}
노가네 = {"나쵸치즈돈까스": 6000, "바베큐치즈돈까스": 5000, "베이컨치즈돈가스": 5000}
홍순두부 = {"차돌순두부찌개": 6000, "해물순두부찌개": 6000, "카레순두부찌개": 6000}
삼삼오오 = {"오삼불고기": 7000, "오삼비빔밥": 5500}
째즈앤라멘 = {"미소라멘": 5000, "닭고기국수": 8000}
돈앤까 = {"돈가스": 6500, "치즈돈가스": 9000, "카레돈가스": 7500}
쇼타돈부리 = {"가츠동": 6500, "믹스동": 7500, "규동": 7000, "가츠카레": 7000}
청춘직화 = {"까망직화불백정식": 7500, "빨강직화불백정식": 7500}
저팔계 = {"당면고기덮밥": 5000, "유부고기덮밥": 5000, "마파두부덮밥": 5000}
천하탕수육 = {"탕수육": 5000, "왕새우튀김": 6000, "수제소세지": 6000}
홍곱창 = {"야채곱창": 12000, "데리야끼막창": 13000, "불곱창": 12000}
샐러드온 = {"그릴드목살샐러드": 5900, "그릴드닭가슴살샐러드": 5900, "파스타샐러드": 5500}
BBQ = {"황금올리브": 17000, "황금올리브닭다리": 19000}
산조메 = {"미소라멘": 7000, "소유라멘": 7000, "규동": 7000}
명륜쭈꾸미 = {"철판쭈꾸미정식": 8000, "불고기덮밥": 7000, "쭈꾸미덮밥": 7000}
casa = {"카르보나라": 10800, "알리고올리오": 10800, "마르게리타피": 11800, "오징어먹물리조또": 14800}
밴프 = {"크림파스타": 6900, "로즈파스타": 6900, "토마토파스타": 6900, "새우볶음밥": 7400}
천향록 = {"마라탕": 9000, "탕수육": 16000, "쯔란양고기": 16000}
페르시안궁전 = {"양갈비카레": 15500, "페르시안케밥": 19000, "데리치킨카레": 11000}
맥덕스 = {"더블치즈피자": 10500, "페퍼로니피자": 10500}
포보 = {"쌀국수": 5000, "로스까스": 5500, "냉모밀": 5000}
맥도날드 = {"맥스파이시상하이세트": 5500, "빅맥세트": 6000}
나누미떡볶이 = {"떡볶이": 4000, "순대": 4000, "김밥": 4000, "어묵": 1000}
따띠삼겹 = {"간단삼겹기본": 2900, "간단삼겹곱빼": 4800}
이삭토스트 = {"불닭토스트": 3800, "베이컨포테이토": 4500, "딥치즈베이컨": 3500}
성균원 = {"짜장면": 4500, "짬뽕": 5000, "탕수육": 12000, "삼선우동": 7500, "사천짜장": 6500}
할매순대국 = {"순대국밥": 6000, "수육국밥": 6000, "얼큰순대국밥": 7000, "순대": 10000}
다발김치찌개 = {"김치찜": 7000, "계란말이": 7000, "김치찌개": 7000}
육십계치킨 = {"고추치킨": 18900, "간지치킨": 18900, "후라이드치킨": 16900, "장스치킨": 18900, "크리스피치킨": 17900}
명륜왕만두 = {
    "고기만두": 3500,
    "고기왕만두": 4000,
    "김치만두": 3500,
    "김치왕만두": 4000,
    "새우찐만두": 4000,
    "새우튀김만두": 5000,
}

# 음식점 리뷰 리스트 =>
후쿠후쿠r = (["깔끔하고 음식량도 많고 맛있어요", "무난한 밥집 저렴함", "걍"],)
노가네r = ["가성비 좋은 돈가스", "성대생들만 아는 맛집"]
홍순두부r = ["순두부 별로 안좋아하는데 맛있게 먹었어요", "재료소진되기 전에 얼른 가세요"]
삼삼오오r = ["가격대비 괜찮은 음식"]
째즈앤라멘r = ["적당한 가격의 일식집"]
돈앤까r = ["신선하지는 않으나 양은 많음"]
쇼타돈부리r = [
    "돈부리 괜찮아요 좋습니다",
    "ㅍㅍ",
    "카레가 생각보다 맵고, 가라아케는 간이 안되어 있음",
    "육회동이 신메뉴인데 너무 별로였다",
    "학교 앞 맛집답게 푸짐해서 좋음",
]
청춘직화r = ["청직 조아 계란줘서 좋다", "두 메뉴의 구성이 알참", "구성이 좋아요 고기는 직화맛 제대로입니다"]
저팔계r = ["단골식당입니다 맛있어요", "중국 현지인이 중국 학생들을 위한 식당", "자극적이지 않은 무난하고 맛있는 중국식 식당"]
천하탕수육r = ["저렴하고 맛있고 친절", "양이 많고 저렴한 가격에 안주로 딱"]
홍곱창r = ["웨이팅 읶는데 기다릴 가치가 있움", "맛있어요", "맛있게 매워요"]
샐러드온r = ["목살샐러드 연어샐러드 좋아해요", "사장님이 친절해요"]
BBQr = ["역시 비비큐", "40분만에 뜨겁게 왔어요"]
산조메r = [""]
명륜쭈꾸미r = ["매콤한 쭈꾸미 생각날떄 가면 좋음", "학교앞이 좋다"]
casar = ["데이트하기 좋아요"]
밴프r = ["나만 알고싶은 가성비 맛집", "양이 많음"]
천향록r = ["한번 들어갔다가 나오면 중국여행 한 기분이에요~"]
페르시안궁전r = ["너무 맛있어요", "맛있고 서비스 친절하십니다"]
맥덕스r = [""]
포보r = ["가성비갑", "돈가스와 쌀국수를 동시에", "양도많고 맛도 좋고 가격도 적당하고"]
맥도날드r = ["맛있어요 배달도 빨라요", "요청사항 다들어주셔서 감동"]
나누미떡볶이r = ["맛있어요", "20년단골맛집", "최고의 떡볶이"]
따띠삼겹r = ["두꺼운 삼겹살", "가격도 싸고 맛있어용", "나쁘지 않아"]
이삭토스트r = ["근처라서 자주 먹어요", "친절하세요", "그냥저냥"]
성균원r = ["배달도 빠르고 맛있어요", "그냥 그래요", "무난"]
할매순대국r = ["양이 예전보다 준 느낌"]
다발김치찌개r = ["양도많고 맛있어요", "배달 김치찌개중 최고"]
육십계치킨r = ["간지치킨 맛있어요"]
명륜왕만두r = ["조금 짠데 짠맛이 맛있네요", "맛있어요~", "성균인의 소울푸드"]


# 음식점 별점 딕셔너리 =>
rating = {
    "후쿠후쿠": 4,
    "노가네": 4,
    "홍순두부": 3,
    "삼삼오오": 5,
    "째즈앤라멘": 3,
    "돈앤까": 2,
    "쇼타돈부리": 3,
    "청춘직화": 4,
    "저팔계": 5,
    "천하탕수육": 4,
    "홍곱창": 5,
    "샐러드온": 5,
    "BBQ": 5,
    "산조메": 0,
    "명륜쭈꾸미": 4,
    "casa 14-2": 4,
    "밴프": 4,
    "천향록": 4,
    "페르시안궁전": 4,
    "맥덕스": 0,
    "포보": 4,
    "맥도날드": 4,
    "나누미떡볶이": 5,
    "따띠삼겹": 4,
    "이삭토스트": 3,
    "성균원": 2,
    "할매순대국": 2,
    "다발 김치찌개": 4,
    "60계치킨": 4,
    "명륜왕만두": 5,
}