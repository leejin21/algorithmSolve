#include <stdlib.h> // atoi, rand, qsort, malloc
#include <stdio.h>
#include <assert.h> // assert
#include <time.h> //time

#define RANGE 10000

typedef struct
{
	int x;
	int y;
} t_point;

typedef struct
{
	t_point from;
	t_point to;
} t_line;

////////////////////////////////////////////////////////////////////////////////
//* DECLARATION OF FUNCTIONS
t_line *upper_hull( t_point *points, int num_point, t_point p1, t_point pn, t_line *lines, int *num_line, int *capacity);
float distance( float a, float b, float c, t_point p);
void separate_points( t_point *points, int num_point, t_point from, t_point to, t_point *s1, t_point *s2, int *n1, int *n2);
////////////////////////////////////////////////////////////////////////////////
// * FUNCTIONS
// TODO upper_hull 함수 제대로 동작하는 지 검증. 이론상으로는 아마 맞을 거임.
// function declaration
// 점들의 집합(points; 점의 수 num_point)에서 점 p1과 점 pn을 잇는 직선의 upper hull을 구하는 함수 (재귀호출)
// [output] lines: convex hull을 이루는 선들의 집합
// [output] num_line: 선의 수
// [output] capacity: lines에 할당된 메모리의 용량 (할당 가능한 선의 수)
// return value: 선들의 집합(lines)에 대한 포인터
t_line *upper_hull( t_point *points, int num_point, t_point p1, t_point pn, t_line *lines, int *num_line, int *capacity){	
	// * SECTION 0. 변수 선언
	int max = 0;
	t_point pmax;
	t_line *new_lines;
	float a, b, c, d;
	
	// * SECTION 1. 메인 알고리즘

	// * SECTION 1-1. 종결 조건: points에 점이 0개 있는 경우
	if (num_point ==0){
		// * SECTION 1-1-1. capacity를 초과하는 경우, 늘려주기
		if (*num_line > *capacity) {
			// * SECTION 1-1-1-1. 새로운 배열 할당: 기존 용량 + 3만큼.
			*capacity = *capacity + 3;
			new_lines = (t_line *) malloc( *capacity * sizeof(t_line));
			// * SECTION 1-1-1-2. 새로운 배열에 기존 배열 내용 복붙
			for (int i=0; i<*num_line; i++){
				new_lines[i] = lines[i];
			}
			// * SECTION 1-1-1-3. 기존 배열 메모리 해제
			free(lines);
		}
		// * SECTION 1-1-2. new_lines로 변수명 통일해주기, 어차피 같은 곳 가리킴.
		else {
			// TODO 실험해 보기. 배열인데 이게 가능? 파이썬은 가능한데..
			// ? 그럼 lines 변수는 가비지값이 될 텐데 어떻게 돌아가는 거지?
			new_lines = lines;
		}
		// * SECTION 1-1-3. new_lines에 점 추가하기.
		new_lines[*num_line].from = p1;
		new_lines[*num_line].to = pn;
		*num_line = *num_line + 1;
		return new_lines;
	} 
	// * SECTION 1-2. 재귀 조건: points에 점이 1개 이상 있는 경우
	else {
		a = - (pn.y - p1.y); b = pn.x - p1.x; c = - p1.x * (pn.y - p1.y) + p1.y * (pn.x - p1.x);
			// ax + by - c = 0 에서 a, b, c 구현한 것
		int n1, n2;

		// * SECTION 1-2-1. pmax 찾아주기
		for (int i=0; i<num_point; i++){
			d = distance(a, b, c, points[i]);
			if (max < d) {
				pmax.x = points[i].x; pmax.y = points[i].y;
			}
		}
		// * SECTION 1-2-2. s1, s2 메모리 할당하고 직선 ax + by -c = 0을 기준으로 나눠 주기
		// s1: set of points, 미리 num_point만큼 메모리 할당 받는 듯
		t_point *s1 = (t_point *)malloc(sizeof(t_point) * num_point);
		assert( s1 != NULL);

		// s2: set of points
		t_point *s2 = (t_point *)malloc(sizeof(t_point) * num_point);
		assert( s2 != NULL);
		
		separate_points(points, num_point, p1, pn, s1, s2, &n1, &n2);


		// * SECTION 1-2-3. s1, s2에 대해 재귀 함수 실행.
		lines = upper_hull( s1, n1, p1, pmax, lines, num_line, capacity);	// upper hull
		lines = upper_hull( s2, n2, pmax, pn, lines, num_line, capacity);	// lower hull
		
		free( s1);
		free( s2);

		return lines;
	}
};

// 직선(ax+by-c=0)과 주어진 점 p(x1, y1) 간의 거리
// distance = |ax1+by1-c| / sqrt(a^2 + b^2)
// 실제로는 sqrt는 계산하지 않음
// return value: 직선과 점 사이의 거리 (분모 제외)
float distance( float a, float b, float c, t_point p){
	float value = a*p.x + b*p.y - c;
	value = value > 0 ? value : -1 * value;		// * 절댓값 구하기
	return value;
};

// 두 점(from, to)을 연결하는 직선(ax + by - c = 0)으로 n개의 점들의 집합 s(점의 수 num_point)를 s1(점의 수 n1)과 s2(점의 수 n2)로 분리하는 함수
// [output] s1 : 직선의 upper(left)에 속한 점들의 집합 (ax+by-c < 0)
// [output] s2 : lower(right)에 속한 점들의 집합 (ax+by-c > 0)
// [output] n1 : s1 집합에 속한 점의 수
// [output] n2 : s2 집합에 속한 점의 수
void separate_points( t_point *points, int num_point, t_point from, t_point to, t_point *s1, t_point *s2, int *n1, int *n2){
	int i, j;
	// * SECTION 두 점을 연결하는 직선 ax + by - c = 0 찾기
	int a, b, c;
	a = - (to.y - from.y); b = to.x - from.x; c = - from.x * (to.y - from.y) + from.y * (to.x - from.x);
	// * SECTION ax + by - c = 0으로 s를 s1과 s2 분리하기
	*n1 = 0; *n2 = 0;
	for (i=0; i<num_point; i++){
		if (a * points[i].x + b * points[i].y - c < 0){
			// s1로 분류되는 경우
			// fprintf( stderr, "%d, ax + by - c = %d\n", i, a * points[i].x + b * points[i].y - c);
			s1[*n1].x = points[i].x; s1[*n1].y = points[i].y;
			// fprintf( stderr, "s1 added:");
			// fprintf( stderr, "original points(%d,%d)\n", points[i].x, points[i].y);
			*n1 = *n1 +1;
		} else if (a * points[i].x + b * points[i].y - c > 0){
			// s2로 분류되는 경우
			// fprintf( stderr, "%d, ax + by - c = %d\n", i, a * points[i].x + b * points[i].y - c);
			s2[*n2].x = points[i].x; s2[*n2].y = points[i].y;
			// fprintf( stderr, "original points(%d,%d)\n", points[i].x, points[i].y);
			// fprintf( stderr, "points(%d,%d)\n", s2[*n2].x, s2[*n2].y);
			*n2 = *n2 + 1;
		}
	}
	// ! (삭제하기) s1, s2 어떻게 분류된 건 지 확인해 주는 코드
	// fprintf( stderr, "s1 added:");
	// for (j=0; j<*n1; j++){
	// 	fprintf( stderr, "points(%d,%d)\n", s1[j].x, s1[j].y);
	// }
	// fprintf( stderr, "s2 added:");
	// for (j=0; j<*n2; j++){
	// 	fprintf( stderr, "points(%d,%d)\n", s2[j].x, s2[j].y);
	// }
};
	


////////////////////////////////////////////////////////////////////////////////
void print_header(char *filename)
{
	printf( "#! /usr/bin/env Rscript\n");
	printf( "png(\"%s\", width=700, height=700)\n", filename);
	
	printf( "plot(1:%d, 1:%d, type=\"n\")\n", RANGE, RANGE);
}

////////////////////////////////////////////////////////////////////////////////
void print_footer(void)
{
	printf( "dev.off()\n");
}

////////////////////////////////////////////////////////////////////////////////
// qsort를 위한 비교 함수
int cmp_x( const void *p1, const void *p2)
{
	t_point *p = (t_point *)p1;
	t_point *q = (t_point *)p2;
	
	float diff = p->x - q->x;
	
    return ((diff >= 0.0) ? ((diff > 0.0) ? +1 : 0) : -1);
}

////////////////////////////////////////////////////////////////////////////////
void print_points( t_point *points, int num_point)
{
	int i;
	printf( "\n#points\n");
	
	for (i = 0; i < num_point; i++)
		printf( "points(%d,%d)\n", points[i].x, points[i].y);
}

////////////////////////////////////////////////////////////////////////////////
void print_line_segments( t_line *lines, int num_line)
{
	int i;

	printf( "\n#line segments\n");
	
	for (i = 0; i < num_line; i++)
		printf( "segments(%d,%d,%d,%d)\n", lines[i].from.x, lines[i].from.y, lines[i].to.x, lines[i].to.y);
}

////////////////////////////////////////////////////////////////////////////////
// [input] points : set of points
// [input] num_point : number of points
// [output] num_line : number of lines
// return value : pointer of set of line segments that forms the convex hull
t_line *convex_hull( t_point *points, int num_point, int *num_line)
{
	int capacity = 10;
	
	t_line *lines = (t_line *) malloc( capacity * sizeof(t_line));
	*num_line = 0;

	// s1: set of points, 미리 num_point만큼 메모리 할당 받는 듯
	t_point *s1 = (t_point *)malloc(sizeof(t_point) * num_point);
	assert( s1 != NULL);

	// s2: set of points
	t_point *s2 = (t_point *)malloc(sizeof(t_point) * num_point);
	assert( s2 != NULL);

	int n1, n2; // number of points in s1, s2, respectively

	// x 좌표에 따라 정렬된 점들의 집합이 입력된 경우
	// points[0] : leftmost point (p1)
	// points[num_point-1] : rightmost point (pn)
	
	// 점들을 분리
	separate_points( points, num_point, points[0], points[num_point-1], s1, s2, &n1, &n2);
	//! (삭제하기) 확인용 코드
	// fprintf(stderr, "n1: %d | n2: %d \n", n1, n2);
	//!
	
	lines = upper_hull( s1, n1, points[0], points[num_point-1], lines, num_line, &capacity);	// upper hull
	lines = upper_hull( s2, n2, points[num_point-1], points[0], lines, num_line, &capacity);	// lower hull
	
	free( s1);
	free( s2);

	return lines;
}

////////////////////////////////////////////////////////////////////////////////
int main( int argc, char **argv)
{
	float x, y;
	int num_point; // number of points
	
	//* SECTION 파일 실행 args 제대로 된 건 지 점검하는 코드
	if (argc != 2)
	{
		// arg로 들어오는 인자 개수 == 2
		printf( "%s number_of_points\n", argv[0]);
		return 0;
	}
	
	num_point = atoi( argv[1]);			// char => int형으로.
	if (num_point <= 0)
	{
		printf( "The number of points should be a positive integer!\n");
		return 0;
	}

	//* SECTION points 배열 생성
	t_point *points;
	points = (t_point *)malloc( sizeof(t_point) * num_point);
	assert( points != NULL);			// points 가 null이면 프로그램 중단
	
	srand( time(NULL));
	for (int i = 0; i < num_point; i++)
	{
		x = rand() % RANGE + 1; 		// 1 ~ RANGE random number
		y = rand() % RANGE + 1;
	
		points[i].x = x;
		points[i].y = y;
 	}
	fprintf( stderr, "%d points created!\n", num_point);
	
	// * SECTION sort the points by their x coordinate
	qsort( points, num_point, sizeof(t_point), cmp_x);

	print_header( "convex.png");
	
	print_points( points, num_point);

	// * SECTION convex hull algorithm
	int num_line;
	
	t_line *lines = convex_hull( points, num_point, &num_line);

	fprintf( stderr, "%d lines created!\n", num_line);
	// ! (삭제하기) 확인용 코드
	// for (int i=0; i<num_line; i++){
		// fprintf( stderr, "segments(%d,%d,%d,%d)\n", lines[i].from.x, lines[i].from.y, lines[i].to.x, lines[i].to.y);
	// }
	// !
	print_line_segments( lines, num_line);
	
	print_footer();
	
	free( points);
	free( lines);
	
	return 0;
}
