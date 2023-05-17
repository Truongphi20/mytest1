# Câu 1
Nên sử dụng kỹ thuật amplicon metagenomics. Vì để xác định thành phần hệ vi sinh nấm có thể sử dụng các vùng gene ITS (*nucler ribosomal internal transcribed spacer*), đây là vùng gene bảo tồn ở nấm giúp phân biệt nấm với các loài khác và cũng đủ phân kỳ để định danh, nghiên cứu về phat sinh loài ở nấm. Bên cạnh đó giúp giảm tiêu hao tài nguyên giải trình tự.

# Câu 2

## QIIME2
Đây là một bộ dụng cụ được tích hợp sẵn các công cụ cần thiết để phân tích amplicon sequencing. 

![](https://docs.qiime2.org/2023.2/_images/overview.png)
Dữ liệu đầu vào gồm có 3 thành phần:
- Sample Data: Bộ dữ liệu được thu thập các đặc tính của các đối tượng mà có thể liên quan đến các câu hỏi sinh học khi nghiên cứu metagenomic (như tuổi, nơi lấy mẫu, kháng sinh,...) 
- FastQ file: Dữ liệu giải trình tự
- Barcode: Dữ liệu về mối liên hệ giữa mẫu và trình tự được giải thông qua barcode (giúp xác định trình tự nào của sample nào).

Dữ liệu đầu vào sẽ được Demultiplex tức trình tự sẽ được link với Sample Data và lưu ở từng file fastq khác nhau tương ứng với các barcode. Sau quá trình này ta sẽ có 1 file Sample Data ban đầu và các file fastq tương ứng với các barcode.

Sau đó trình tự được lọc nhiễu, loại bỏ các bias của phản ứng PCR xác định các OTU hoặc ASV đại diện cho sự hiện diện của đối tượng trong mẫu. Sau quá trình này thu được Feature Table và Các trình tự. Các trình tự có thể dùng phân tích phát sinh loài, xác định các loài trong mẫu. Bên cạnh đó có thể sử dụng Feature Table để phân tích thêm Diversity $\alpha$ và $\beta$,...

![](https://scontent.fsgn5-5.fna.fbcdn.net/v/t1.15752-9/344680192_252335350676523_2726603943882926596_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=AzKMmyZ8kmgAX8aJguU&_nc_ht=scontent.fsgn5-5.fna&oh=03_AdR0NsNI2TGSDFi-amSGLZp1NAov_NvgphecCm62GitiNw&oe=648C0CC6)

### _Ưu điểm_
   
- Công cụ linh hoạt, có thể tùy pipline thay đổi linh hoạt dựa trên input và câu hỏi sinh học.
- Có cộng đồng phân tích đông đảo, có thể trao đổi thông tin.
- Mã nguồn mở, miễn phí, dễ dàng tiếp cận, mở rộng.
- Kiểm soát pipeline, nguồn trích dẫn được lưu trong artifact data. 

### _Nhược điểm_
- Có những thuật toán thống kê phức tạp, đòi hỏi kiến thức tối thiểu về toán
- Khi có bug, cần trao đồi cần phải chờ phản hồi.

## USEARCH-VSEARCH

![](https://scontent.fsgn5-12.fna.fbcdn.net/v/t1.15752-9/344668763_1161796954498196_518117829784371646_n.png?_nc_cat=103&ccb=1-7&_nc_sid=ae9488&_nc_ohc=XLhSlZPMmukAX8uKHMK&_nc_ht=scontent.fsgn5-12.fna&oh=03_AdQuyK9xyNkL2Tn4vjetjM8bvQabO7VkC396ELCdlQ6nqQ&oe=648C07E0)

Cũng tương tự như QUIIME, với USEARCH, mục tiêu đầu hướng tói cũng là chuyển trình tự thô thành Feature Table. Dữ liệu cũng sẽ được kết hợp với nhau và chọn các trình tự đại diện nhằm giảm sự bias về số lượng mẫu trong phân tích. Với USEARCH sẽ tạo thành các OTU bằng các nhóm các trình tự tương đồng, quy về OTU, và các bước downstream có thể phân tích tương tự như QIIME. 

![](https://scontent.fsgn8-2.fna.fbcdn.net/v/t1.15752-9/344668767_1254000772155956_909791682515151533_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=jPtYQk1ethgAX8QwvbP&_nc_ht=scontent.fsgn8-2.fna&oh=03_AdTHEih-ZTAEbQWeE1y_ra4suFEFedTBTJyeWo96fmCnWw&oe=648BEC2A)

### _Ưu điểm_
 - Được phát triển trước QIIME
 - Miễn phí, mã nguồn mở
 - Linh động, có thể tùy chỉnh 

### _Nhược điểm_
 - Cộng đồng nghiên cứu ít (công bố 78 bài báo liên quan trong khi QIIME là 231 bài báo) 
 - Giao diện trang chủ đơn giản, ít thu hút.

        Theo em công cụ QIIME thích hợp hơn với công ty hơn nhờ những tính năng vượt trội của đó, có tiềm năng phát triển hơn trong tương lai. Công cụ linh hoạt dễ phân công chia việc, tạo pipline với workflow, documment chi tiết, cộng động sử dụng đông đảo.

# Câu 3

Trong các artifact data của QIIME2 thực chất là các file zip. Dữ liệu bên trong dễ dàng được unzip sử  để sử dụng, lập trình thêm các công cụ bổ sung bằng python, bash, nextflow,... Ngoài ra phần mềm còn hỗ trợ tương tác trực tiếp thông qua python bằng Jupyter Notebook hoặc Galaxy Workflow. Ở bước nghiên cứu Diversity có thể phát triển thêm các công cụ trực quan hóa dữ liệu có thể webapp, giúp dễ dàng truy cập và sử dụng.

# Câu 4

[![](https://mermaid.ink/img/pako:eNo1UDFuhDAQ_Iq1NSBjMGAXaXJdlCpXRIEUFjYHCmAERglBPOaSF6S9lPeS-0nsO6XZnRnNzkqzQqmlAg5Vq9_LWowG7XdFP-j8ob6cvjWazkfzaoUwfz5_LUhefn_6A-q0nFvldJLf16p8Qy7G8SjfX05HjYzW7WQFl-X7d0PoBnEHDkTgQafGTjTS_l6LHqECTK06VQC3UKpKzK0poOg3axWz0U9LXwI346w8mAcpjNo14jCKDngl2smqg-hftO7-TZYCX-EDOCFpkIZhRnBCszhKKfVgAe7jgCYszgjJIsYwThjdPPi8RuCAhTTGlBGGs8yuxAMlG6PHx1tf19q2P-pvaXs?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNo1UDFuhDAQ_Iq1NSBjMGAXaXJdlCpXRIEUFjYHCmAERglBPOaSF6S9lPeS-0nsO6XZnRnNzkqzQqmlAg5Vq9_LWowG7XdFP-j8ob6cvjWazkfzaoUwfz5_LUhefn_6A-q0nFvldJLf16p8Qy7G8SjfX05HjYzW7WQFl-X7d0PoBnEHDkTgQafGTjTS_l6LHqECTK06VQC3UKpKzK0poOg3axWz0U9LXwI346w8mAcpjNo14jCKDngl2smqg-hftO7-TZYCX-EDOCFpkIZhRnBCszhKKfVgAe7jgCYszgjJIsYwThjdPPi8RuCAhTTGlBGGs8yuxAMlG6PHx1tf19q2P-pvaXs)

Đầu tiên cần khảo sát thị trường về nhu cầu visualize dữ liệu. Xem những hướng visualize nào đã và đang phát triển, những hướng vẫn còn chưa phát triển. Thu thập, Xây dựng dần các module hỗ trợ trực quan hóa. Check tính năng và sự chính xác của các module. Sau đó lắp ráp các module tạo thành các công cụ web app giúp người dùng dễ dàng truy cập và sử dụng. 

Các tiêu chí đánh giá:
- Câu hỏi sinh học có tính lặp lại ở các khách hàng hay không?
- Đã có công cụ đã phát triển chưa? Nếu có công cụ đó đã tối ưu chưa?
- Ứng dụng đã xây dựng có lượt sử dụng bao nhiêu? Số lượng bài báo công bố liên quan?