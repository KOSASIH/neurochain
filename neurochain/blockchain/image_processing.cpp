#include <opencv2/opencv.hpp>

int main() {
    cv::Mat image = cv::imread("image.jpg");
    cv::Mat gray;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);

    cv::Mat edges;
    cv::Canny(gray, edges, 50, 150);

    cv::Mat contours;
    cv::findContours(edges, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    for (int i = 0; i < contours.size(); i++) {
        cv::drawContours(image, contours, i, cv::Scalar(0, 255, 0), 2);
    }

    cv::imshow("Image", image);
    cv::waitKey(0);
    cv::destroyAllWindows();
    return 0;
}
