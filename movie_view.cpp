#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/core/utility.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

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

    std::string name = "Effect";
    cv::namedWindow(name, cv::WINDOW_AUTOSIZE);
    int fps = int(capture.get(cv::CAP_PROP_FPS));

    while(true){
        cv::Mat frame;
        capture >> frame;

        if (frame.empty())
            break;

        cv::imshow(name, frame);
        frame.release();
        
        int key = cv::waitKey(fps);
        if (key == 27)
            break;

    }

    capture.release();
    cv::destroyAllWindows();
    
    return 0;
}
