---
title: Màn hình riêng cho máy tính bảng
description: Vì sao Sunmeld trên máy tính bảng không chỉ là màn hình điện thoại bị kéo giãn, và chúng tôi kiểm tra nhiều kích thước màn hình như thế nào.
slug: tablet-layouts
lang: vi
category: devlog
keywords: Sunmeld, iPad, bố cục, kích thước màn hình, kiểm thử, nhật ký
translation_of: en
---
Sunmeld vẫn đang được phát triển cho iOS và Android. Ghi chép này nói về chuyện xảy ra khi cùng một trò chơi gặp một màn hình lớn hơn nhiều.

## Lần thử đầu tiên: một chiếc điện thoại ở giữa

Ban đầu, trên máy tính bảng trò chơi chỉ hiện màn hình điện thoại trong một cột hẹp ở giữa. Mọi thứ đều chạy được, nhưng phần lớn màn hình bị bỏ trống. Xoay máy tính bảng ngang thì nó thành một màn hình điện thoại bị kéo rộng ra. Như vậy đủ để thử trò chơi, nhưng không đủ để chơi.

## Hai bố cục, không phải một

Giờ đây chúng tôi vẽ máy tính bảng bằng hai bố cục riêng, dọc và ngang. Ở chế độ dọc, thùng lớn hơn, đối thủ ở phía trên và bạn ở phía dưới. Ở chế độ ngang, đối thủ ở bên trái, thùng ở giữa và bạn ở bên phải. Màn hình kết quả đặt hình ảnh ở một bên, còn điểm số và các nút ở bên kia. Điện thoại vẫn giữ màn hình riêng như trước. Chúng tôi chọn bố cục dựa vào chiều rộng của cửa sổ, không dựa vào tên thiết bị.

## Kiểm tra các kích thước mà không cần cả một ngăn kéo thiết bị

Chúng tôi không thể cầm trên tay mọi chiếc máy tính bảng, nên bố cục được kiểm tra bằng các bài kiểm tra tự động: chúng vẽ các màn hình ở nhiều kích thước điện thoại và máy tính bảng, chiều dọc lẫn chiều ngang, và báo lỗi nếu có gì bị tràn hoặc nếu chọn phải một bố cục ngoài dự kiến. Những kiểm tra này chạy giống hệt nhau cho cả 12 ngôn ngữ, vì một từ dài trong ngôn ngữ này có thể làm hỏng bố cục vốn trông ổn ở ngôn ngữ khác. Chúng tôi cũng giữ một vài ảnh chụp thật từ trình giả lập máy tính bảng để tự mắt xem xét.

## Một cái bẫy nhỏ trong công cụ

Một điều bất ngờ nằm ở các công cụ chụp màn hình. Trên hệ điều hành máy tính bảng mới hơn, trình giả lập có thể mở ứng dụng ngang trong một cửa sổ thay vì xoay thiết bị, nên ảnh chụp ra bị nằm ngang. Giờ chúng tôi cố ý vẽ màn hình xoay cho những ảnh đó, rồi xoay lại tệp cho thẳng.

## Những gì chưa được kiểm tra

Chúng tôi chưa xem một ván chơi bị xoay giữa chừng trên máy tính bảng thật, và những cửa sổ hẹp gần bằng điện thoại sẽ quay về bố cục điện thoại, mà chúng tôi cũng chưa xem kỹ. Khi có thay đổi, chúng tôi sẽ nói ở đây. Hiện chưa có ngày phát hành.

## Câu hỏi thường gặp

### Máy tính bảng có bố cục riêng không?

Có. Máy tính bảng dùng bố cục dọc và ngang riêng, được chọn theo chiều rộng cửa sổ chứ không theo tên thiết bị. Điện thoại vẫn giữ màn hình riêng.

### Làm sao kiểm tra được nhiều kích thước màn hình như vậy?

Các bài kiểm tra tự động vẽ màn hình ở nhiều kích thước điện thoại và máy tính bảng, cả dọc lẫn ngang, cho cả 12 ngôn ngữ.

### Đã thử xoay màn hình giữa ván trên máy tính bảng thật chưa?

Chưa. Chúng tôi chưa từng thấy một ván bị xoay giữa chừng trên máy tính bảng thật.

### Đã có ngày phát hành chưa?

Chưa. Hiện chưa có ngày phát hành.
