---
title: Dấu "kỷ lục mới" sau một trận luyện tập
description: Khi nào màn hình kết quả hiện kỷ lục mới, những kỷ lục nào được tính, và dấu hiệu xuất hiện thế nào.
slug: new-record
lang: vi
category: devlog
keywords: Sunmeld, kỷ lục mới, kết quả, chuỗi thắng, luyện tập, nhật ký
translation_of: en
---
Sunmeld vẫn đang được phát triển cho iOS và Android. Ghi chú này nói về một dấu nhỏ trên màn hình kết quả, xuất hiện khi một trận luyện tập lập kỷ lục mới.

## Vì sao cần dấu trên màn hình kết quả

Kỷ lục chỉ có ích khi bạn nhận ra nó. Trước thay đổi này, điểm cao nhất hay chuỗi thắng dài nhất có thể tăng mà màn hình kết quả không có dấu hiệu nào. Vì vậy chúng tôi thêm một dòng phía trên phần tóm tắt, ghi "Kỷ lục mới", kèm các kỷ lục mà trận này đã lập.

## Chỉ hiện những gì đã tăng

Dòng này chỉ liệt kê các kỷ lục đã tăng trong trận này: điểm cao nhất ở mức khó và chuỗi thắng dài nhất. Nếu không có gì tăng, dòng không xuất hiện. Chiến thắng đầu tiên ở mức khó cũng được tính là kỷ lục mới.

## Chuỗi bắt đầu từ hai

Chuỗi chỉ được hiện khi chuỗi dài nhất đạt ít nhất hai. Nếu không, mỗi chiến thắng đầu tiên sẽ đều hiện dấu, và dấu đó không cho biết điều gì.

## Chỉ trận luyện tập

Trận giải đấu, thử thách hằng ngày và chế độ rush không cộng vào kỷ lục luyện tập, nên cũng không hiện dấu. Chạm "Chơi lại" sẽ xóa dấu, để dấu cũ không được mang sang trận tiếp theo.

## Cách dấu xuất hiện

Dấu lớn dần từ kích thước nhỏ hơn một chút đến kích thước đầy đủ. Khi tắt chuyển động trong hệ thống hoặc trong ứng dụng, dấu hiện ngay ở kích thước đầy đủ mà không chuyển động. Dấu dùng cùng kiểu thẻ như dấu "kỷ lục mới" trong chế độ xếp chồng đơn và rush.

## Những điều chưa kiểm tra

Chúng tôi chưa xem dấu hiển thị thế nào trên thiết bị thật, cũng chưa biết trình đọc màn hình đọc nó ra sao. Trên màn hình rất nhỏ, có thể cần cuộn thêm một chút để chạm được các nút. Hiện chưa có ngày phát hành.

## Câu hỏi thường gặp

### Dấu có hiện trong trận giải đấu không?

Không. Trận giải đấu, thử thách hằng ngày và rush đều không hiện dấu này.

### Những gì được tính là kỷ lục mới?

Điểm cao nhất ở mức khó được nâng lên, hoặc chuỗi thắng dài nhất được kéo dài hơn. Chiến thắng đầu tiên ở mức khó cũng được tính.

### Vì sao chuỗi thắng cần hai trận?

Chuỗi một trận sẽ trùng với mọi chiến thắng đầu tiên. Bắt đầu từ hai giúp dấu vẫn có ý nghĩa.

### Có ngày phát hành chưa?

Chưa. Chưa có ngày nào được đặt.
