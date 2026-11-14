---
title: Liệu mặt trời có bao giờ xuất hiện?
description: Chuyện gì xảy ra khi chúng tôi cho người chơi AI chơi Sunmeld hết lần này đến lần khác: viên đá cao nhất gần như không bao giờ xuất hiện, và cách sửa nằm ở luật chơi chứ không phải ở AI.
slug: can-the-sun-appear
lang: vi
category: devlog
keywords: Sunmeld, cân bằng, AI, kiểm thử, thiết kế game, nhật ký
translation_of: en
---
Sunmeld vẫn đang được phát triển cho iOS và Android. Ghi chép này nói về một vấn đề mà chúng tôi chỉ phát hiện ra vì không tin vào cảm giác của chính mình về trò chơi.

## Để các AI chơi cho đến cùng

Thuở đầu, luật chơi chỉ là một bản nguyên mẫu làm nhanh. Trước khi mời ai thử, chúng tôi cho các người chơi AI đấu với nhau rất nhiều ván, mỗi lần đều bắt đầu từ cùng một điều kiện để kết quả có thể lặp lại. Chúng tôi theo dõi xem bao nhiêu ván kết thúc vì tràn thùng, người đi trước thắng bao nhiêu lần, và có bao nhiêu lần ai đó tạo ra được viên đá cao nhất, tức mặt trời.

## Mặt trời không bao giờ xuất hiện

Với luật của bản nguyên mẫu, không ai từng tạo ra mặt trời. Không phải AI dễ, cũng không phải AI mạnh nhất. Thoạt tiên có vẻ đây là vấn đề của AI, nên chúng tôi xem xét AI. Rồi chúng tôi quay sang tính toán.

Mỗi lần hợp nhất gộp hai viên đá thành một viên của cấp kế tiếp, nên mặt trời chứa rất nhiều "thể tích đá". Những viên đá rơi vào thùng lại là những viên nhỏ. Với số lượt thả mà một ván cho phép, tổng thể tích có thể đi vào thùng thấp hơn nhiều so với mức một mặt trời cần. Dù giỏi đến đâu cũng không thể xây nên thứ mà luật chơi không cấp đủ vật liệu. Đây là vấn đề của luật chơi, không phải của AI.

## Chúng tôi đã đổi gì

Chúng tôi định hình lại thang cấp và kích thước thùng, đồng thời cấp cho mỗi người chơi một số lượt thả phù hợp với thang cấp mới. Sau đó, cũng những ván AI ấy đã tạo ra mặt trời, với các AI mạnh hơn thì thường xuyên hơn, và ít ván kết thúc vì tràn thùng hơn. Mặt trời trở nên hiếm nhưng có thể xuất hiện, đúng như chúng tôi muốn ở một cấp cuối cùng.

## Điều bất ngờ thứ hai: đồng hồ ngắm

Các lượt chạy thử còn cho thấy một ván chơi theo thời gian thực kết thúc vì tràn thùng thường xuyên hơn cùng ván đó khi chơi tức thì. Đó không phải lỗi của AI. Đồng hồ tràn thùng vẫn chạy trong lúc người chơi còn đang ngắm, nên người vừa thả đá vào một chiếc thùng đã chật có thể thua trong khi phía bên kia đang suy nghĩ. Giờ đây đồng hồ báo nguy sẽ dừng lại khi người chơi đang ngắm.

## Vì sao chúng tôi kể điều này

Nếu tự thử bằng tay, chúng tôi sẽ mất rất lâu mới nhận ra mặt trời nằm ngoài tầm với. Vài dòng tính toán và rất nhiều ván tự động đã tìm ra điều đó chỉ trong một buổi chiều. Hiện chưa có ngày phát hành. Khi có tin, bạn sẽ thấy nó ở đây.
