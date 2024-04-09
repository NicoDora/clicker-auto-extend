import { Injectable } from '@nestjs/common';
import { UserRepository } from '../repositories/user.repository';
import { FindOneOptions } from 'typeorm';
import { User } from 'src/entities/User';

@Injectable()
export class UserService {
  constructor(private readonly userRepository: UserRepository) {}

  createUser(stdNum: string, password: string) {
    return this.userRepository.createUser(stdNum, password);
  }

  findUser(options: FindOneOptions<User>) {
    return this.userRepository.findUser(options);
  }

  async updateUser(stdNum: string, password: string) {
    const response = await this.userRepository.updateUser(stdNum, password);
    if (response.affected) {
      return { message: 'User updated successfully' };
    }
  }
}
