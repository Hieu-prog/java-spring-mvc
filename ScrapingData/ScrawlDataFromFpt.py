import os
from bs4 import BeautifulSoup
import mysql.connector
import requests
# Kết nối tới MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="laptopshop1"
)

cursor = conn.cursor()

# Danh sách các file HTML tương ứng với các param
html_files = {

    "GAMING": r"C:\Users\Nguyen Duc Hieu\Downloads\scraping_data\.venv\html_files\Gaming.html",
    "SINHVIEN-VANPHONG": r"C:\Users\Nguyen Duc Hieu\Downloads\scraping_data\.venv\html_files\sv_vanphong.html",
    "MONG-NHE": r"C:\Users\Nguyen Duc Hieu\Downloads\scraping_data\.venv\html_files\mong-nhe.html",
    "DOANH-NHAN": r"C:\Users\Nguyen Duc Hieu\Downloads\scraping_data\.venv\html_files\doanh-nhan.html"
}

base_url = 'https://fptshop.com.vn'

# Duyệt qua các file HTML tương ứng với từng param và target
for target, file_name in html_files.items():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            page_content = file.read()

        # Phân tích nội dung HTML bằng BeautifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')

        # Lấy tất cả tên sản phẩm hoặc thông tin (tùy vào cấu trúc của HTML)
        products = soup.find_all('div', class_='ProductCard_cardInfo__r8zG4')
        print(f"Có: {len(products)} sản phẩm")
        if not products:
            print(f"Đã lấy hết sản phẩm cho {target}.")
            continue  # Bỏ qua nếu không còn sản phẩm

        for product in products:
            shortDesc = product.find('a', title=True)
            if shortDesc:
                quantity = 100
                sold = 0

                shortDesc_text = shortDesc.text.strip()

                # Cắt từ sau Laptop để lấy factory
                processed_desc = shortDesc_text.strip()

                if "Laptop" in processed_desc:
                    words = processed_desc.split("Laptop", 1)[1].strip().split()
                    if words:
                        factory = words[0]
                    else:
                        factory = "Apple"
                else:
                    factory = "Apple"

                # Cắt 6 từ đầu tiên làm tên sản phẩm
                words = shortDesc_text.split()
                name = ' '.join(words[:6])  # Lấy 6 từ đầu tiên và ghép lại thành chuỗi

                # Lấy giá sản phẩm
                price = product.find('p', class_='Price_currentPrice__PBYcv')
                if price:
                    price_text = price.text.strip().replace('₫', '').replace('.', '').replace(',', '')
                    try:
                        price_float = float(price_text)
                    except ValueError:
                        price_float = 0.0
                else:
                    price_float = 0.0

                # Lấy link chi tiết sản phẩm
                detail_url = shortDesc['href']
                print({detail_url})
                # Gửi yêu cầu đến trang chi tiết sản phẩm để lấy detailDesc
                detail_response = requests.get(detail_url)
                if detail_response.status_code == 200:
                    detail_response.encoding = 'utf-8'
                    detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

                    # Lấy ảnh từ trang chi tiết
                    div_tag = detail_soup.find('div', class_='swiper-zoom-container')
                    if div_tag:
                        img_tag = div_tag.find('img')
                        if img_tag:
                            img_url = img_tag.get('src', None)
                        else:
                            img_url = None
                    else:
                        img_url = None

                    # Lấy mô tả sản phẩm (cần cập nhật theo class thực tế)
                    description_div = detail_soup.find('div', class_='description-container')
                    if description_div:
                         detailDesc = description_div.find('p')
                         if detailDesc:
                             detail_desc_text = detailDesc.text.strip()
                         else:
                            detail_desc_text = "Không có mô tả"
                    else:
                        detail_desc_text = "Không có mô tả"

                    # Chèn dữ liệu vào bảng MySQL
                    query = """
                    INSERT INTO products (detail_desc, factory, image, name, price, quantity, short_desc, sold, target)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    data = (detail_desc_text, factory, img_url, name, price_float, quantity, shortDesc_text, sold, target)
                    cursor.execute(query, data)
                    conn.commit()  # Lưu thay đổi vào cơ sở dữ liệu
                else:
                    print(f"Không thể truy cập trang chi tiết {detail_url}.")
            else:
                print(f"Không thể truy cập sản phẩm.")

    except FileNotFoundError:
        print(f"File {file_name} không tìm thấy.")
        continue

# Đóng kết nối
cursor.close()
conn.close()
