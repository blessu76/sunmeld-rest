---
title: Công tắc âm thanh không làm gì cả
description: Vì sao cài đặt âm thanh của Sunmeld im lặng một thời gian, và chúng tôi đã thêm gì để có thể nghe thấy tiếng khi hợp nhất.
slug: sound-that-was-silent
lang: vi
category: devlog
keywords: Sunmeld, âm thanh, âm thanh game, cài đặt, chế độ im lặng, nhật ký
translation_of: en
---
Sunmeld vẫn đang được phát triển cho iOS và Android. Ghi chú này nói về một cài đặt đã có nhưng không thể làm gì.

## Công tắc có đó, âm thanh thì không

Màn hình cài đặt có một công tắc âm thanh, và nó lưu lựa chọn của bạn đúng cách. Trò chơi kiểm tra công tắc này mỗi lần một viên đá rơi xuống hoặc hợp nhất. Nhưng phần đáng lẽ phát âm thanh chỉ là một chỗ giữ chỗ trống. Chúng tôi cố ý để như vậy vì tệp âm thanh và giấy phép chưa được quyết định. Bản thân công tắc chưa bao giờ hỏng. Thứ còn thiếu là âm thanh.

## Tự tạo âm thanh

Thay vì chờ giấy phép, chúng tôi tự tạo âm thanh. Có mười sáu hiệu ứng ngắn cho những việc như đá chạm đáy, hợp nhất, chuỗi liên tiếp và cảnh báo tràn. Chúng được tạo bởi một kịch bản nhỏ không dùng số ngẫu nhiên, nên chạy hai lần sẽ cho cùng một tệp. Tổng cộng khoảng 220 KB.

## Im lặng khi điện thoại im lặng

Trò chơi được thiết lập để tôn trọng công tắc im lặng trên iPhone, và không làm dừng nhạc của ứng dụng khác đang phát. Trên Android, âm thanh phát như âm thanh trò chơi và không giành tiêu điểm âm thanh. Nếu một âm thanh không phát được, ván chơi vẫn tiếp tục bình thường.

## Những gì chúng tôi chưa nghe

Âm thanh đã được kết nối và ứng dụng có thể được xây dựng cùng chúng. Nhưng chúng tôi chưa nghe thử trên một chiếc iPhone thật, trong một căn phòng thật, ở âm lượng bình thường. Âm sắc và độ to có thể cần chỉnh thêm một lần nữa. Khi đó, chỉ cần thay tệp âm thanh bằng tệp khác cùng tên.

## Câu hỏi thường gặp

### Trước đây vì sao không có âm thanh?

Đầu ra âm thanh là một chỗ giữ chỗ im lặng. Các tệp âm thanh và phần âm thanh của ứng dụng chỉ mới được thêm gần đây.

### Trò chơi có tôn trọng công tắc im lặng trên iPhone không?

Đó là cách nó được thiết lập. Chúng tôi chưa kiểm tra trên thiết bị thật; khi làm xong, chúng tôi sẽ nói thêm.

### Tôi có thể tắt âm thanh không?

Có. Công tắc âm thanh trong cài đặt điều khiển các hiệu ứng. Khi tắt, trò chơi không phát gì cả.
