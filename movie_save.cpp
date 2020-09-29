#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/core/utility.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/videoio.hpp>

int main(int argc, const char* argv[])
{
    cv::String keys = "{src||}""{cascade||}";
    cv::CommandLineParser parser(argc, argv, keys);
    cv::String src_path = parser.get<cv::String>("src");

    cv::VideoCapture capture(src_path);
    if (!capture.isOpened()){
        //error in opening the video input
        std::cerr << "Unable to open file!" << std::endl;
        return 0;
    }

    /* 初期設定 */
    int cap_width = int(capture.get(cv::CAP_PROP_FRAME_WIDTH));
    int cap_height = int(capture.get(cv::CAP_PROP_FRAME_HEIGHT));
    int fps = int(capture.get(cv::CAP_PROP_FPS));
    int fourcc = cv::VideoWriter::fourcc('m','p','4','v');
    cv::Size video_size = cv::Size(cap_width,cap_height);

    cv::VideoWriter writer("output.mp4", fourcc, fps, video_size);

    while(true){
        cv::Mat frame;
        capture >> frame;

        if (frame.empty())
            break;

        writer << frame;
        frame.release();
    }

    capture.release();
    writer.release();

    return 0;
}
