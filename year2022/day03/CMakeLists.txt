cmake_minimum_required(VERSION 3.0.0)
project(day03 VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

add_executable(solution main.cpp solution.cpp)
add_executable(test_solution solution_test.cpp solution.cpp)

# target_include_directories(test_solution PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
add_test(NAME test_solution COMMAND test_solution)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
