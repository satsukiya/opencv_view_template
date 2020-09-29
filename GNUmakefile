CXX = c++
CXXFLAGS =  -I/usr/local/Cellar/opencv/4.3.0_3/include/opencv4/
LDFLAGS = -L/usr/local/Cellar/opencv/4.3.0_3/lib/
LDLIBS =  -lopencv_core -lopencv_imgcodecs  -lopencv_highgui -lopencv_imgproc -lopencv_videoio
CXXVERSION = -std=c++11

main: main.cpp
	$(CXX) $< -o $@ $(CXXFLAGS) $(CXXVERSION) $(LDFLAGS) $(LDLIBS)

movie_save: movie_save.cpp
	$(CXX) $< -o $@ $(CXXFLAGS) $(CXXVERSION) $(LDFLAGS) $(LDLIBS)

clean :
	rm out
