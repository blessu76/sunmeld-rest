---
title: Xem lại ván đã kết thúc, từng nước một
description: Tính năng xem lại một ván Sunmeld đã kết thúc hoạt động thế nào và chúng tôi đã kiểm tra rằng nó chạy lại giống hệt ra sao.
slug: replay
lang: vi
category: devlog
keywords: Sunmeld, xem lại, phát lại, ván chơi, nhật ký
translation_of: en
---
Sunmeld vẫn đang được phát triển cho iOS và Android. Ghi chú này nói về một tính năng cho phép bạn xem lại ván đã kết thúc, từng nước một.

## Vì sao muốn xem lại

Khi ván kết thúc, người ta tự hỏi vì sao mình thua. Bạn biết viên đá cuối cùng đã tràn, nhưng khó nhớ mọi thứ bắt đầu nghiêng từ đâu. Vì vậy chúng tôi thêm "Xem lại" vào màn hình kết quả.

## Chúng tôi ghi nước đi, không phải video

Ván chơi không được quay thành video. Chúng tôi chỉ ghi những gì cần để dựng lại: giá trị ngẫu nhiên lúc bắt đầu, ai đi trước, và với mỗi viên đá thả xuống thì rơi ở bước nào, đặt ở đâu và là loại đá gì. Viên đá tự rơi khi hết giờ cũng được ghi theo cách đó.

## Đưa lại vào cùng một bước

Khi bạn nhấn "Xem lại", các nước đã lưu được đưa lại vào bộ máy trò chơi ở cùng các bước. Cùng đầu vào cho cùng kết quả. Không chỉ điểm số mà vị trí và giai đoạn của mọi viên đá cũng phải khớp, và một bài kiểm tra tự động cố định điều đó. Các bài kiểm tra gồm đá rơi do hết giờ, đá đặc biệt, ván do đối thủ đi trước và việc đọc lại bản ghi đã lưu.

## Cách xem

Có phát và tạm dừng, bắt đầu lại và nước tiếp theo, và bạn có thể đổi giữa tốc độ chậm hơn và nhanh hơn. Nếu bật giảm chuyển động trong hệ thống hoặc trong ứng dụng, phần xem lại bắt đầu ở trạng thái dừng và không có hiệu ứng ánh sáng. Khi đó bạn có thể đi từng nước một bằng "Nước tiếp theo".

## Giới hạn hiện tại

Chỉ các ván với đối thủ AI mới xem lại được. Chế độ xếp một mình và ván luyện tập không nằm trong đó. Chỉ xem được ván gần nhất, và lối vào duy nhất là màn hình kết quả. Chuyển động ngắm của AI không được vẽ lại; viên đá đi thẳng tới nơi nó rơi. Kết quả của cú rơi vẫn như vậy.

## Điều chúng tôi chưa kiểm tra

Chúng tôi chưa kiểm tra cảm giác trên thiết bị thật hay âm thanh khi dùng trình đọc màn hình. Chúng tôi cũng chưa biết bản ghi lớn đến đâu với một ván rất dài. Nếu có thay đổi, chúng tôi sẽ ghi ở đây. Chưa có ngày phát hành.

## Câu hỏi thường gặp

### Tôi có thể xem lại ván trước không?

Bạn có thể xem lại ván gần nhất đã kết thúc với đối thủ AI từ màn hình kết quả.

### Phần xem lại có thể ra kết quả khác không?

Không. Các nước đã lưu được đưa lại ở cùng các bước, và các bài kiểm tra xác nhận điểm số cùng vị trí của mọi viên đá khớp nhau.

### Tôi có xem lại được chế độ xếp một mình không?

Chưa. Hiện chỉ hỗ trợ các ván với đối thủ AI.

### Đã có ngày phát hành chưa?

Chưa. Chưa ấn định ngày phát hành.
