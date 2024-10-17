import yaml

def read_yaml_file(level: str) -> list:
    """
    Đọc file YAML và trả về danh sách câu hỏi theo level người dùng yêu cầu.
    
    Tham số:
        level (str): Cấp độ câu hỏi cần lấy ('1', '2', '3') 
        Có ba mức độ kiểm tra: 1 (dễ) , 2 (trung bình), 3(khó) đã thông báo cho người dùng trước đó 
    
    Trả về:
        list: Danh sách các câu hỏi theo level yêu cầu
    """
    try:
        # Mở và đọc file YAML
        with open('questions.yaml', 'r') as file:
            data = yaml.safe_load(file)

        # Kiểm tra xem level có tồn tại trong dữ liệu không
        if level not in data:
            print(f"Không tìm thấy câu hỏi cho cấp độ '{level}'", "bạn có thể gọi lại lệnh /kiemtra và chọn cấp độ khác")
            return []

        # Trả về danh sách câu hỏi theo level
        return data[level]

    except FileNotFoundError:  #lỗi không tìm thấy file
        print("File 'questions.yaml' không tồn tại!")
        return []
    except yaml.YAMLError as e: #lỗi file trình bày không đúng định dạng
        print(f"Lỗi khi đọc file YAML: {e}")
        return []

# Kiểm thử hàm
level = "1" #level 1 = dễ 
questions = read_yaml_file(level)

if questions: # chỗ này phần so sánh số lượng câu hỏi và trộn để đưa ra các câu hỏi để trích xuất mình vẫn chưa xử lý được
    print(f"Các câu hỏi cho level '{level}':")
    for q in questions:
        print(f"- Câu hỏi: {q['question']}")
        print("  Các lựa chọn:")
        for opt in q["options"]:
            print(f"   {opt}")
        print(f"  Đáp án đúng: {q['answer']}")
else:
    print(f"Không có câu hỏi nào cho cấp độ '{level}'.")
