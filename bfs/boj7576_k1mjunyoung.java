package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 1트 실패: 예외처리 안함
 * 2트 실패: 시간 초과 -> 단순 순회할 때도 bfs를 사용해보자
 *
 */
public class boj7576_k1mjunyoung {
    static int N, M;
    static int[][] box;
    static boolean[][] isVisited;
    static boolean[][] isGrowCurrently;

    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = { 0, 1, 0,-1};

    static class Pos {
        int y;
        int x;

        Pos(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // M = scanner.nextInt();
        // N = scanner.nextInt();
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        box = new int[N][M];
        isVisited = new boolean[N][M];
        isGrowCurrently = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                // ox[i][j] = scanner.nextInt();
                box[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int count = 0;

        boolean isAllGrown = !isExistZeroTomato();

        Root:
        while (!isAllGrown) {
            // 돌면서 익히기
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (box[i][j] == 1 && !isVisited[i][j] && !isGrowCurrently[i][j]) {
                        growUp(i, j);
                    }
                }
            }

            count++;
            isGrowCurrently = new boolean[N][M];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (box[i][j] == 0) {
                        if (canGrow(i, j)) {
                            continue Root;
                        } else {
                            count = -1;
                        }
                    }
                }
            }

            isAllGrown = true;
        }

        System.out.println(count);
    }

    static void growUp(int y, int x) {
        Pos pos = new Pos(y, x);

        for (int d = 0; d < 4; d++) {
            int ny = pos.y + dy[d];
            int nx = pos.x + dx[d];

            if (ny < 0 || ny >= N || nx < 0 || nx >= M) {
                continue;
            }
            if (box[ny][nx] == -1 || box[ny][nx] == 1) {
                continue;
            }
            if (isVisited[ny][nx]) {
                continue;
            }

            box[ny][nx] = 1;
            isGrowCurrently[ny][nx] = true;
        }

        isVisited[pos.y][pos.x] = true;
    }

    static boolean isExistZeroTomato() {
        boolean zeroTomato = false;

        Check:
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (box[i][j] == 0) {
                    zeroTomato = true;
                    break Check;
                }
            }
        }

        return zeroTomato;
    }

    static boolean canGrow(int y, int x) {
        boolean isPossible = true;

        int direction = 4;

        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            if (ny < 0 || ny >= N || nx < 0 || nx >= M) {
                direction--;
                continue;
            }
            if (box[ny][nx] == -1) {
                direction--;
            }
        }

        if (direction < 1) {
            isPossible = false;
        }

        return isPossible;
    }
}
