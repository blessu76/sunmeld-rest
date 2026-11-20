---
title: Đưa những viên đá lên một động cơ trò chơi
description: Vì sao những viên đá rơi và các phần chuyển động khác của Sunmeld nay chạy trên một động cơ trò chơi, và chúng tôi đã kiểm tra thế nào.
slug: stones-on-a-game-engine
lang: vi
category: devlog
keywords: Sunmeld, Flame, động cơ, hoạt ảnh, hiệu năng, nhật ký
translation_of: en
published: 2026-11-20T16:00+09:00
---
Sunmeld vẫn đang được phát triển cho iOS và Android. Ghi chú này nói về cách các phần chuyển động của trò chơi được vẽ.

## Trước hết, liệt kê mọi chuyển động

Trước khi thay đổi gì, chúng tôi ghi lại mọi chuyển động trong trò chơi: những viên đá rơi và va chạm, ánh sáng khi đá hợp nhất, điểm số hiện lên, vạch cảnh báo, vạch ngắm và thanh trên cùng với điểm và thời gian. Với mỗi thứ, chúng tôi hỏi nó tốn bao nhiêu công việc cho màn hình trong mỗi khung hình. Có thứ nhẹ. Có thứ nặng, chẳng hạn vẽ lại một viên đá với chuyển màu và ánh sáng mềm ở mỗi khung hình.

## Vẽ một lần, di chuyển nhiều lần

Động cơ chúng tôi chọn là Flame, một động cơ trò chơi chạy trên Flutter. Những viên đá và tấm kính nay được vẽ thành hình ảnh một lần, rồi đặt vào mỗi khung hình. Ánh sáng khi hợp nhất là một hình mềm có sẵn với màu phủ lên trên. Chữ điểm số được chuẩn bị trước. Luật chơi không đổi: cùng một vật lý vẫn xử lý việc rơi và hợp nhất.

## Đã kiểm tra trên máy tính, chưa trên điện thoại

Chúng tôi đo trên một chiếc Mac ở chế độ profile, và các khung hình vẫn nằm trong ngân sách thời gian. Đó là máy tính, không phải điện thoại của bạn. Chúng tôi chưa kiểm tra kết quả trên iPhone hoặc Android thật ở tần số làm mới tối đa, nên độ mượt trên thiết bị thật vẫn còn để ngỏ.

## Vì sao chọn động cơ

Các công cụ vẽ của chính Flutter cũng làm được điều này. Chúng tôi không chạy thử so sánh song song, nên không khẳng định động cơ nhanh hơn. Chúng tôi chọn nó vì mọi phần chuyển động nay chạy trong một vòng lặp, giúp dễ giữ mượt hơn khi trò chơi lớn lên.

## Tiếp theo là gì

Bước cuối là kiểm tra cảm giác trên thiết bị thật có tần số làm mới cao, và xem lại các màn hình nhỏ. Hiện chưa có ngày phát hành.

## Câu hỏi thường gặp

### Cách chơi có thay đổi không?

Không. Luật chơi và vật lý được giữ nguyên. Chỉ có cách vẽ và thời điểm của các phần chuyển động thay đổi.

### Vì sao dùng động cơ trò chơi?

Mọi phần chuyển động nay chạy trong một vòng lặp, nên trò chơi không phải dựng lại cả màn hình cho mỗi chuyển động nhỏ.

### Đã thử trên điện thoại chưa?

Cho đến nay mới đo trên máy tính. Bài kiểm tra trên điện thoại thật vẫn còn ở phía trước.
