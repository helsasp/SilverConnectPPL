import apiClient from './api.js';

class ProfileService {
  async getProfilePageData(userId) {
    try {
      const [userDetailsResponse, postsResponse, connectionsResponse] = await Promise.all([
        apiClient.get(`/users/${userId}`),          // Endpoint untuk detail user
        apiClient.get(`/users/${userId}/posts`),    // Endpoint untuk postingan user
        apiClient.get(`/users/${userId}/connections`) // Endpoint untuk teman/koneksi user
      ]);

      return {
        userDetails: userDetailsResponse.data,
        posts: postsResponse.data,
        connections: connectionsResponse.data,
      };
    } catch (error) {
      console.error("Failed to fetch profile page data:", error);
      throw error;
    }
  }

  async updateProfile(userId, profileData) {
    return apiClient.put(`/users/${userId}`, profileData);
  }
}

export default new ProfileService();