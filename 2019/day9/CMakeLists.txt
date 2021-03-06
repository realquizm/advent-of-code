cmake_minimum_required(VERSION 3.10) 

project(day9)

# Set sources to be compiled
set( MAIN_SOURCES "cpp/src/main.cpp" )

# Compile the sources
add_executable (${PROJECT_NAME} ${MAIN_SOURCES} )

# Give the relative path of the compilation as SOURCE_DIR
target_compile_definitions(${PROJECT_NAME} 
                           PUBLIC SOURCE_DIR="${CMAKE_CURRENT_SOURCE_DIR}")
# Link intcode
target_link_libraries(${PROJECT_NAME} intcode)

# Build tests
set( TEST_SOURCES "cpp/tests/day9_test.cpp")
set ( TEST_TARGET ${PROJECT_NAME}_tests)

# Test exectuable
add_executable (${TEST_TARGET} ${TEST_SOURCES} ${SOURCES})
target_link_libraries(${TEST_TARGET} gtest gtest_main intcode)
target_compile_definitions(${TEST_TARGET} 
                           PUBLIC SOURCE_DIR="${CMAKE_CURRENT_SOURCE_DIR}")
set_target_properties(${TEST_TARGET} PROPERTIES EXCLUDE_FROM_ALL TRUE)

# Set up test
add_test( ${PROJECT_NAME}_test ${TEST_TARGET})
add_dependencies(build_tests ${TEST_TARGET})
