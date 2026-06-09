def add_reward_points(current_points, points_earned):
    """Hàm tính tổng điểm mới bằng cách cộng điểm thưởng vào điểm hiện tại."""
    return current_points + points_earned

# Khởi tạo điểm số trong phạm vi cục bộ (Local/Main scope)
initial_points = 100
reward = 50

# Truyền giá trị vào hàm và nhận lại kết quả cập nhật
final_points = add_reward_points(initial_points, reward)

print("Đã cộng thêm", reward, "điểm.")
print("Tổng điểm hiện tại của khách hàng:", final_points)