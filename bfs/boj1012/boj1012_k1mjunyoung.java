package array.boj1012;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * https://www.acmicpc.net/problem/1012
 */
public class boj1012_k1mjunyoung {
    // 상 우 하 좌
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {-1, 0, 1, 0};

    static int N, M;
    static int[][] field;
    static int[][] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 테스트 케이스의 개수
        int T = Integer.parseInt(br.readLine());

        for (int test = 0; test < T; test++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            // 가로길이
            M = Integer.parseInt(st.nextToken());
            // 세로길이
            N = Integer.parseInt(st.nextToken());

            field = new int[N][M];
            check = new int[N][M];

            // 배추가 심어진 위치의 개수
            int K = Integer.parseInt(st.nextToken());

            // 밭 생성
            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                field[Y][X] = 1;
            }

            // 필요한 지렁이 수
            int worm = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (field[i][j] == 1 && check[i][j] != 1) {
                        bfs(i ,j);
                        worm++;
                    }
                }
            }

            System.out.println(worm);
        }
    }

    static void bfs(int x, int y) {
        Queue<Pos> queue = new LinkedList<>();
        queue.offer(new Pos(x, y));
        check[x][y] = 1;

        // 배추가 있는 좌표 check[][]에 저장
        while (!queue.isEmpty()) {
            Pos pos = queue.poll();

            for (int k = 0; k < 4; k++) {
                int nx = pos.x + dx[k];
                int ny = pos.y + dy[k];

                if (nx < 0 || nx >= M || ny < 0 || ny >= N) {
                    continue;
                }

                if (field[ny][nx] == 1 && check[ny][nx] != 1) {
                    queue.offer(new Pos(nx, ny));
                    check[ny][nx] = 1;
                }
            }
        }
    }
}
class Pos {
    int x;
    int y;

    Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
