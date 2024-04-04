import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity('user')
export class User {
  @PrimaryGeneratedColumn({
    type: 'int',
    name: 'id',
    comment: '유저 고유 ID',
    unsigned: true,
  })
  id: number;

  @Column({
    type: 'varchar',
    name: 'std_num',
    comment: '학번',
    length: 100,
  })
  stdNum: string;

  @Column({
    type: 'varchar',
    name: 'password',
    comment: '비밀번호',
    length: 100,
  })
  password: string;

  @Column({
    type: 'timestamp',
    name: 'created_at',
    comment: '생성시간',
    default: () => 'CURRENT_TIMESTAMP',
  })
  createdAt: Date;

  @Column({
    type: 'timestamp',
    name: 'deleted_at',
    comment: '삭제시간',
    default: () => 'CURRENT_TIMESTAMP',
  })
  deletedAt: Date;
}
